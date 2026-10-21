# EMA Hourly Continuation — TNSR/USDT P12_100

**Symbol:** TNSR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.8095 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 0.9801 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -1.6841 |
| sortino_ratio | -0.5485 |
| max_drawdown | 0.5234 |
| cagr | -0.2259 |
| net_avg_win | 78.0549 |
| net_avg_loss | -93.1896 |
| avg_hold_time_bars | 23.4231 |
| exposure | 0.5586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
