# EMA Hourly Continuation — BSV/USDT P50_144

**Symbol:** BSV/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.4308 |
| net_win_rate | 0.3963 |
| gross_profit_factor | 0.7250 |
| gross_win_rate | 0.4111 |
| sharpe_ratio | -6.2824 |
| sortino_ratio | -2.0551 |
| max_drawdown | 0.9191 |
| cagr | -0.6326 |
| net_avg_win | 32.5036 |
| net_avg_loss | -49.5293 |
| avg_hold_time_bars | 13.1389 |
| exposure | 0.3225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
