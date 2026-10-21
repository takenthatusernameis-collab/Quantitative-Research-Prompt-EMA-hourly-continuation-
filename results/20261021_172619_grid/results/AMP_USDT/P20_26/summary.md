# EMA Hourly Continuation — AMP/USDT P20_26

**Symbol:** AMP/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.4012 |
| net_win_rate | 0.3759 |
| gross_profit_factor | 0.6170 |
| gross_win_rate | 0.3759 |
| sharpe_ratio | -4.7103 |
| sortino_ratio | -1.1159 |
| max_drawdown | 0.7383 |
| cagr | -0.4040 |
| net_avg_win | 47.3134 |
| net_avg_loss | -71.0331 |
| avg_hold_time_bars | 4.5949 |
| exposure | 0.0572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
