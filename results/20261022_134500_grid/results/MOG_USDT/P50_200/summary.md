# EMA Hourly Continuation — MOG/USDT P50_200

**Symbol:** MOG/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.7450 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 0.9608 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -1.8433 |
| sortino_ratio | -0.5126 |
| max_drawdown | 0.4751 |
| cagr | -0.2129 |
| net_avg_win | 71.4362 |
| net_avg_loss | -92.6696 |
| avg_hold_time_bars | 21.0710 |
| exposure | 0.3687 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
