# EMA Hourly Continuation — DGB/USDT P89_200

**Symbol:** DGB/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.5771 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.8947 |
| gross_win_rate | 0.4675 |
| sharpe_ratio | -3.8038 |
| sortino_ratio | -1.1568 |
| max_drawdown | 0.7579 |
| cagr | -0.4226 |
| net_avg_win | 48.8520 |
| net_avg_loss | -69.9304 |
| avg_hold_time_bars | 10.2987 |
| exposure | 0.2163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
