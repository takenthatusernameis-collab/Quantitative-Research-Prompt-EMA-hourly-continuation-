# EMA Hourly Continuation — 1INCH/USDT P20_89

**Symbol:** 1INCH/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.6800 |
| net_win_rate | 0.4702 |
| gross_profit_factor | 0.8883 |
| gross_win_rate | 0.4702 |
| sharpe_ratio | -2.7551 |
| sortino_ratio | -0.8673 |
| max_drawdown | 0.6497 |
| cagr | -0.3282 |
| net_avg_win | 58.6151 |
| net_avg_loss | -76.5132 |
| avg_hold_time_bars | 18.7125 |
| exposure | 0.4142 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
