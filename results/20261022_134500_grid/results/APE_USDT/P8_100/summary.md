# EMA Hourly Continuation — APE/USDT P8_100

**Symbol:** APE/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.6340 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.9555 |
| gross_win_rate | 0.4738 |
| sharpe_ratio | -4.0333 |
| sortino_ratio | -1.4160 |
| max_drawdown | 0.8240 |
| cagr | -0.4942 |
| net_avg_win | 48.4557 |
| net_avg_loss | -66.6424 |
| avg_hold_time_bars | 24.1081 |
| exposure | 0.6893 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
