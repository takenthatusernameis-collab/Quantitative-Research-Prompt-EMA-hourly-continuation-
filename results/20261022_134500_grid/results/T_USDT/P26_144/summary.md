# EMA Hourly Continuation — T/USDT P26_144

**Symbol:** T/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.6437 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.9551 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -3.3291 |
| sortino_ratio | -1.0368 |
| max_drawdown | 0.7178 |
| cagr | -0.3922 |
| net_avg_win | 54.9846 |
| net_avg_loss | -77.8050 |
| avg_hold_time_bars | 19.5456 |
| exposure | 0.4361 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
