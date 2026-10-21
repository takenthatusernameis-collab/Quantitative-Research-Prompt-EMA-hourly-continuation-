# EMA Hourly Continuation — STX/USDT P55_144

**Symbol:** STX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.7489 |
| net_win_rate | 0.4905 |
| gross_profit_factor | 0.9341 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -1.4806 |
| sortino_ratio | -0.3749 |
| max_drawdown | 0.3632 |
| cagr | -0.1581 |
| net_avg_win | 67.7815 |
| net_avg_loss | -87.1326 |
| avg_hold_time_bars | 16.5601 |
| exposure | 0.2368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
