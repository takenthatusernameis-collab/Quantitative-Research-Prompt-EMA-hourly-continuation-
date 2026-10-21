# EMA Hourly Continuation — MEW/USDT P12_89

**Symbol:** MEW/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.7509 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.8952 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -1.9238 |
| sortino_ratio | -0.6175 |
| max_drawdown | 0.5330 |
| cagr | -0.2474 |
| net_avg_win | 63.2907 |
| net_avg_loss | -77.2888 |
| avg_hold_time_bars | 22.5965 |
| exposure | 0.5218 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
