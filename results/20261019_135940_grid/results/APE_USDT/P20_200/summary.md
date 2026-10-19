# EMA Hourly Continuation — APE/USDT P20_200

**Symbol:** APE/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.7283 |
| net_win_rate | 0.4975 |
| gross_profit_factor | 0.9810 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -1.7943 |
| sortino_ratio | -0.5150 |
| max_drawdown | 0.4552 |
| cagr | -0.2134 |
| net_avg_win | 60.0991 |
| net_avg_loss | -81.7061 |
| avg_hold_time_bars | 32.7931 |
| exposure | 0.6052 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
