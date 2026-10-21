# EMA Hourly Continuation — BTT/USDT P89_144

**Symbol:** BTT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.4150 |
| net_win_rate | 0.3985 |
| gross_profit_factor | 0.7168 |
| gross_win_rate | 0.3985 |
| sharpe_ratio | -4.9733 |
| sortino_ratio | -1.1846 |
| max_drawdown | 0.7604 |
| cagr | -0.4320 |
| net_avg_win | 49.8238 |
| net_avg_loss | -79.5425 |
| avg_hold_time_bars | 10.1476 |
| exposure | 0.1250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
