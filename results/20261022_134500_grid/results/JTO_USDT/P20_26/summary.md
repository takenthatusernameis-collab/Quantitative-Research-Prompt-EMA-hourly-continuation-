# EMA Hourly Continuation — JTO/USDT P20_26

**Symbol:** JTO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1247 |
| net_profit_factor | 0.3652 |
| net_win_rate | 0.4050 |
| gross_profit_factor | 0.8577 |
| gross_win_rate | 0.4419 |
| sharpe_ratio | -11.5900 |
| sortino_ratio | -5.8332 |
| max_drawdown | 0.9994 |
| cagr | -0.9484 |
| net_avg_win | 11.3864 |
| net_avg_loss | -21.2187 |
| avg_hold_time_bars | 2.1379 |
| exposure | 0.1212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
