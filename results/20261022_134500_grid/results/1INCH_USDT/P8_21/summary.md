# EMA Hourly Continuation — 1INCH/USDT P8_21

**Symbol:** 1INCH/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1684 |
| net_profit_factor | 0.3386 |
| net_win_rate | 0.4097 |
| gross_profit_factor | 0.7709 |
| gross_win_rate | 0.4525 |
| sharpe_ratio | -13.5353 |
| sortino_ratio | -7.8912 |
| max_drawdown | 1.0000 |
| cagr | -0.9821 |
| net_avg_win | 7.4199 |
| net_avg_loss | -15.2106 |
| avg_hold_time_bars | 3.0695 |
| exposure | 0.2350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
