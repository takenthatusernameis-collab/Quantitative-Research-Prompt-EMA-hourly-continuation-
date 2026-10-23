# EMA Hourly Continuation — AMP/USDT P8_21

**Symbol:** AMP/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 2067 |
| net_profit_factor | 0.2191 |
| net_win_rate | 0.3425 |
| gross_profit_factor | 0.6133 |
| gross_win_rate | 0.3841 |
| sharpe_ratio | -18.5078 |
| sortino_ratio | -12.0122 |
| max_drawdown | 1.0000 |
| cagr | -0.9980 |
| net_avg_win | 3.9637 |
| net_avg_loss | -9.4233 |
| avg_hold_time_bars | 2.7088 |
| exposure | 0.2545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
