# EMA Hourly Continuation — FIL/USDT P50_144

**Symbol:** FIL/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.7522 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9567 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -1.5794 |
| sortino_ratio | -0.3982 |
| max_drawdown | 0.4019 |
| cagr | -0.1673 |
| net_avg_win | 73.5958 |
| net_avg_loss | -93.5322 |
| avg_hold_time_bars | 17.8071 |
| exposure | 0.2517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
