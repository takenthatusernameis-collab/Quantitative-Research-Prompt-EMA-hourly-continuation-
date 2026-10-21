# EMA Hourly Continuation — MNT/USDT P12_50

**Symbol:** MNT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.7216 |
| net_win_rate | 0.5059 |
| gross_profit_factor | 1.0106 |
| gross_win_rate | 0.5059 |
| sharpe_ratio | -2.3883 |
| sortino_ratio | -0.8363 |
| max_drawdown | 0.6274 |
| cagr | -0.3186 |
| net_avg_win | 53.2431 |
| net_avg_loss | -75.5425 |
| avg_hold_time_bars | 13.3008 |
| exposure | 0.3597 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
