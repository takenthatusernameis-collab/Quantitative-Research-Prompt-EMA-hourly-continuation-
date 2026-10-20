# EMA Hourly Continuation — AXL/USDT P26_89

**Symbol:** AXL/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 798 |
| net_profit_factor | 0.5867 |
| net_win_rate | 0.4336 |
| gross_profit_factor | 0.8945 |
| gross_win_rate | 0.4461 |
| sharpe_ratio | -5.8269 |
| sortino_ratio | -2.2956 |
| max_drawdown | 0.9420 |
| cagr | -0.6743 |
| net_avg_win | 38.6076 |
| net_avg_loss | -50.3714 |
| avg_hold_time_bars | 8.5627 |
| exposure | 0.3092 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
