# EMA Hourly Continuation — WIF/USDT P26_50

**Symbol:** WIF/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 970 |
| net_profit_factor | 0.6077 |
| net_win_rate | 0.4732 |
| gross_profit_factor | 0.9490 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -5.8042 |
| sortino_ratio | -2.5417 |
| max_drawdown | 0.9597 |
| cagr | -0.7089 |
| net_avg_win | 32.2304 |
| net_avg_loss | -47.6380 |
| avg_hold_time_bars | 3.6948 |
| exposure | 0.1629 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
