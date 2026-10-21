# EMA Hourly Continuation — ENJ/USDT P12_89

**Symbol:** ENJ/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.6635 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 0.9967 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -3.7968 |
| sortino_ratio | -1.3963 |
| max_drawdown | 0.8259 |
| cagr | -0.4850 |
| net_avg_win | 48.3956 |
| net_avg_loss | -68.5909 |
| avg_hold_time_bars | 17.9092 |
| exposure | 0.5535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
