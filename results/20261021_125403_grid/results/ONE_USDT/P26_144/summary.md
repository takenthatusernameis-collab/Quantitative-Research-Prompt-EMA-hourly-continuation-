# EMA Hourly Continuation — ONE/USDT P26_144

**Symbol:** ONE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.8450 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0019 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.0317 |
| sortino_ratio | -0.2752 |
| max_drawdown | 0.3424 |
| cagr | -0.1208 |
| net_avg_win | 86.5810 |
| net_avg_loss | -102.4584 |
| avg_hold_time_bars | 33.0259 |
| exposure | 0.5224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
