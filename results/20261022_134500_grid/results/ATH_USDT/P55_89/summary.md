# EMA Hourly Continuation — ATH/USDT P55_89

**Symbol:** ATH/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.4479 |
| net_win_rate | 0.4431 |
| gross_profit_factor | 0.7725 |
| gross_win_rate | 0.4538 |
| sharpe_ratio | -6.1112 |
| sortino_ratio | -2.2821 |
| max_drawdown | 0.9271 |
| cagr | -0.6673 |
| net_avg_win | 26.0610 |
| net_avg_loss | -46.2886 |
| avg_hold_time_bars | 3.8692 |
| exposure | 0.1219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
