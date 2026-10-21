# EMA Hourly Continuation — W/USDT P55_144

**Symbol:** W/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.8142 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 0.9925 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -1.1556 |
| sortino_ratio | -0.3035 |
| max_drawdown | 0.3216 |
| cagr | -0.1316 |
| net_avg_win | 77.3670 |
| net_avg_loss | -95.5933 |
| avg_hold_time_bars | 15.5786 |
| exposure | 0.2386 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
