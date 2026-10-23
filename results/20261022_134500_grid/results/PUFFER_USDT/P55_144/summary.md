# EMA Hourly Continuation — PUFFER/USDT P55_144

**Symbol:** PUFFER/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.6284 |
| net_win_rate | 0.4653 |
| gross_profit_factor | 0.8781 |
| gross_win_rate | 0.4703 |
| sharpe_ratio | -3.1952 |
| sortino_ratio | -1.0120 |
| max_drawdown | 0.6359 |
| cagr | -0.3785 |
| net_avg_win | 55.4929 |
| net_avg_loss | -76.8592 |
| avg_hold_time_bars | 11.0817 |
| exposure | 0.2534 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
