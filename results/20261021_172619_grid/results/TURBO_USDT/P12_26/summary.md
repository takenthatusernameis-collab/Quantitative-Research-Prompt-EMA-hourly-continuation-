# EMA Hourly Continuation — TURBO/USDT P12_26

**Symbol:** TURBO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.8964 |
| net_win_rate | 0.5437 |
| gross_profit_factor | 1.1816 |
| gross_win_rate | 0.5437 |
| sharpe_ratio | -0.6956 |
| sortino_ratio | -0.2112 |
| max_drawdown | 0.2502 |
| cagr | -0.0959 |
| net_avg_win | 82.6777 |
| net_avg_loss | -109.9067 |
| avg_hold_time_bars | 5.0082 |
| exposure | 0.1000 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
