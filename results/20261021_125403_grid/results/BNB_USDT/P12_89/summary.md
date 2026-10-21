# EMA Hourly Continuation — BNB/USDT P12_89

**Symbol:** BNB/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.6260 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9730 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -3.2584 |
| sortino_ratio | -0.9884 |
| max_drawdown | 0.6896 |
| cagr | -0.3669 |
| net_avg_win | 51.9310 |
| net_avg_loss | -79.7020 |
| avg_hold_time_bars | 25.8352 |
| exposure | 0.5273 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
