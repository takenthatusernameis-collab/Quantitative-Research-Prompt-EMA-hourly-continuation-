# EMA Hourly Continuation — LISTA/USDT P55_89

**Symbol:** LISTA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.7124 |
| net_win_rate | 0.4852 |
| gross_profit_factor | 0.9417 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -2.0673 |
| sortino_ratio | -0.5634 |
| max_drawdown | 0.4622 |
| cagr | -0.2285 |
| net_avg_win | 68.6175 |
| net_avg_loss | -90.7853 |
| avg_hold_time_bars | 8.6686 |
| exposure | 0.1433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
