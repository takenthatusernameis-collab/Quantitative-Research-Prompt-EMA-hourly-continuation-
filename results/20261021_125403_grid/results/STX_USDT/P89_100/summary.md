# EMA Hourly Continuation — STX/USDT P89_100

**Symbol:** STX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 93 |
| net_profit_factor | 0.5821 |
| net_win_rate | 0.4516 |
| gross_profit_factor | 0.8155 |
| gross_win_rate | 0.4516 |
| sharpe_ratio | -1.5866 |
| sortino_ratio | -0.2178 |
| max_drawdown | 0.2316 |
| cagr | -0.0952 |
| net_avg_win | 73.9500 |
| net_avg_loss | -104.6275 |
| avg_hold_time_bars | 4.5484 |
| exposure | 0.0191 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
