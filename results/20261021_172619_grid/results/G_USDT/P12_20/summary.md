# EMA Hourly Continuation — G/USDT P12_20

**Symbol:** G/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.6370 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0225 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -3.4889 |
| sortino_ratio | -1.1853 |
| max_drawdown | 0.6933 |
| cagr | -0.4172 |
| net_avg_win | 50.4640 |
| net_avg_loss | -79.2234 |
| avg_hold_time_bars | 5.3646 |
| exposure | 0.1354 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
