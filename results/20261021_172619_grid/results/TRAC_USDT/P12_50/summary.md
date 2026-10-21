# EMA Hourly Continuation — TRAC/USDT P12_50

**Symbol:** TRAC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.7141 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.9073 |
| gross_win_rate | 0.4710 |
| sharpe_ratio | -2.6513 |
| sortino_ratio | -0.9006 |
| max_drawdown | 0.6684 |
| cagr | -0.3387 |
| net_avg_win | 60.2187 |
| net_avg_loss | -75.0801 |
| avg_hold_time_bars | 12.0457 |
| exposure | 0.3115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
