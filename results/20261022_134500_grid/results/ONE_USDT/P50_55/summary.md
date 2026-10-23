# EMA Hourly Continuation — ONE/USDT P50_55

**Symbol:** ONE/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 840 |
| net_profit_factor | 0.2460 |
| net_win_rate | 0.3571 |
| gross_profit_factor | 0.8009 |
| gross_win_rate | 0.3976 |
| sharpe_ratio | -12.3228 |
| sortino_ratio | -5.2586 |
| max_drawdown | 0.9990 |
| cagr | -0.9372 |
| net_avg_win | 10.8622 |
| net_avg_loss | -24.5353 |
| avg_hold_time_bars | 1.7095 |
| exposure | 0.0653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
