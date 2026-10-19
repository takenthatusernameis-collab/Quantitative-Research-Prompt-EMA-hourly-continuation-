# EMA Hourly Continuation — ETHFI/USDT P8_50

**Symbol:** ETHFI/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1087 |
| net_profit_factor | 0.5706 |
| net_win_rate | 0.4508 |
| gross_profit_factor | 0.8641 |
| gross_win_rate | 0.4572 |
| sharpe_ratio | -5.9452 |
| sortino_ratio | -2.7495 |
| max_drawdown | 0.9640 |
| cagr | -0.7321 |
| net_avg_win | 26.1234 |
| net_avg_loss | -37.5787 |
| avg_hold_time_bars | 9.4839 |
| exposure | 0.4686 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
