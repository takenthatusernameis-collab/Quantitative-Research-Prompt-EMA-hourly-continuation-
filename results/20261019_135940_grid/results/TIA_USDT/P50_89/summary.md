# EMA Hourly Continuation — TIA/USDT P50_89

**Symbol:** TIA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 619 |
| net_profit_factor | 0.6255 |
| net_win_rate | 0.4701 |
| gross_profit_factor | 0.9529 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -4.1209 |
| sortino_ratio | -1.4532 |
| max_drawdown | 0.8231 |
| cagr | -0.4971 |
| net_avg_win | 47.1784 |
| net_avg_loss | -66.9185 |
| avg_hold_time_bars | 4.9935 |
| exposure | 0.1405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
