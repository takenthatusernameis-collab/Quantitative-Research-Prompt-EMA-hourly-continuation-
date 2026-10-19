# EMA Hourly Continuation — LTC/USDT P8_34

**Symbol:** LTC/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1383 |
| net_profit_factor | 0.3159 |
| net_win_rate | 0.4309 |
| gross_profit_factor | 0.8474 |
| gross_win_rate | 0.4642 |
| sharpe_ratio | -11.2077 |
| sortino_ratio | -5.8542 |
| max_drawdown | 0.9995 |
| cagr | -0.9520 |
| net_avg_win | 7.7459 |
| net_avg_loss | -18.5663 |
| avg_hold_time_bars | 5.1244 |
| exposure | 0.3221 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
