# EMA Hourly Continuation — WIF/USDT P12_50

**Symbol:** WIF/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1100 |
| net_profit_factor | 0.7087 |
| net_win_rate | 0.4809 |
| gross_profit_factor | 1.0595 |
| gross_win_rate | 0.4918 |
| sharpe_ratio | -5.2225 |
| sortino_ratio | -2.4292 |
| max_drawdown | 0.9517 |
| cagr | -0.6925 |
| net_avg_win | 43.6191 |
| net_avg_loss | -57.0176 |
| avg_hold_time_bars | 6.4409 |
| exposure | 0.3220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
