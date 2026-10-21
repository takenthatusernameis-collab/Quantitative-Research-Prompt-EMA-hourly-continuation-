# EMA Hourly Continuation — WIF/USDT P50_144

**Symbol:** WIF/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.8119 |
| net_win_rate | 0.4953 |
| gross_profit_factor | 0.9644 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -1.0909 |
| sortino_ratio | -0.2785 |
| max_drawdown | 0.2903 |
| cagr | -0.1219 |
| net_avg_win | 76.1199 |
| net_avg_loss | -92.0038 |
| avg_hold_time_bars | 17.1755 |
| exposure | 0.2490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
