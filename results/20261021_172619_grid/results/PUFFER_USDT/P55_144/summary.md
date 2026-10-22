# EMA Hourly Continuation — PUFFER/USDT P55_144

**Symbol:** PUFFER/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.7927 |
| net_win_rate | 0.4919 |
| gross_profit_factor | 0.9615 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -1.3938 |
| sortino_ratio | -0.3896 |
| max_drawdown | 0.3280 |
| cagr | -0.1650 |
| net_avg_win | 77.2473 |
| net_avg_loss | -94.3220 |
| avg_hold_time_bars | 13.9088 |
| exposure | 0.2416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
