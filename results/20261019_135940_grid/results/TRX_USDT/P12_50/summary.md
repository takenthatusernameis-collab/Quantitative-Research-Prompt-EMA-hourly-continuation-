# EMA Hourly Continuation — TRX/USDT P12_50

**Symbol:** TRX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 934 |
| net_profit_factor | 0.2956 |
| net_win_rate | 0.3844 |
| gross_profit_factor | 1.0178 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -12.3807 |
| sortino_ratio | -5.5002 |
| max_drawdown | 0.9995 |
| cagr | -0.9493 |
| net_avg_win | 11.6821 |
| net_avg_loss | -24.6753 |
| avg_hold_time_bars | 7.4657 |
| exposure | 0.3170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
