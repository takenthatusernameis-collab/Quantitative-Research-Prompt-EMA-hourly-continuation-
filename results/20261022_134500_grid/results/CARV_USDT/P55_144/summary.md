# EMA Hourly Continuation — CARV/USDT P55_144

**Symbol:** CARV/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.4816 |
| net_win_rate | 0.4386 |
| gross_profit_factor | 0.7888 |
| gross_win_rate | 0.4474 |
| sharpe_ratio | -4.4164 |
| sortino_ratio | -1.2738 |
| max_drawdown | 0.7160 |
| cagr | -0.4577 |
| net_avg_win | 44.0376 |
| net_avg_loss | -71.4333 |
| avg_hold_time_bars | 11.5263 |
| exposure | 0.2218 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
