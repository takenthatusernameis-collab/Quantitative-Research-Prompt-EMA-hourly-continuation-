# EMA Hourly Continuation — WOO/USDT P21_34

**Symbol:** WOO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1085 |
| net_profit_factor | 0.4865 |
| net_win_rate | 0.4295 |
| gross_profit_factor | 0.9822 |
| gross_win_rate | 0.4562 |
| sharpe_ratio | -9.1222 |
| sortino_ratio | -4.2756 |
| max_drawdown | 0.9949 |
| cagr | -0.8771 |
| net_avg_win | 20.2274 |
| net_avg_loss | -31.2993 |
| avg_hold_time_bars | 2.9392 |
| exposure | 0.1450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
