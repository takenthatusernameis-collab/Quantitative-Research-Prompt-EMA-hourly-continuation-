# EMA Hourly Continuation — SNX/USDT P55_144

**Symbol:** SNX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.8778 |
| net_win_rate | 0.5259 |
| gross_profit_factor | 1.1094 |
| gross_win_rate | 0.5259 |
| sharpe_ratio | -0.7457 |
| sortino_ratio | -0.2001 |
| max_drawdown | 0.3010 |
| cagr | -0.0906 |
| net_avg_win | 83.6236 |
| net_avg_loss | -105.6547 |
| avg_hold_time_bars | 14.5316 |
| exposure | 0.2288 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
