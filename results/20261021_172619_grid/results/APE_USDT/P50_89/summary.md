# EMA Hourly Continuation — APE/USDT P50_89

**Symbol:** APE/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.6485 |
| net_win_rate | 0.4640 |
| gross_profit_factor | 0.8599 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -2.6175 |
| sortino_ratio | -0.7228 |
| max_drawdown | 0.5756 |
| cagr | -0.2820 |
| net_avg_win | 59.8720 |
| net_avg_loss | -79.9255 |
| avg_hold_time_bars | 7.3920 |
| exposure | 0.1260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
