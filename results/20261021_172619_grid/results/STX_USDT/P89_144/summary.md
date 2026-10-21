# EMA Hourly Continuation — STX/USDT P89_144

**Symbol:** STX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.8342 |
| net_win_rate | 0.5269 |
| gross_profit_factor | 1.0939 |
| gross_win_rate | 0.5269 |
| sharpe_ratio | -0.8332 |
| sortino_ratio | -0.1935 |
| max_drawdown | 0.2358 |
| cagr | -0.0860 |
| net_avg_win | 74.4954 |
| net_avg_loss | -99.4690 |
| avg_hold_time_bars | 8.1692 |
| exposure | 0.0961 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
