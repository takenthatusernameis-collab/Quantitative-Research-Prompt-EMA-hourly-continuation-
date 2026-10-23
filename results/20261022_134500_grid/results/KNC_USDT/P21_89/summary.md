# EMA Hourly Continuation — KNC/USDT P21_89

**Symbol:** KNC/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.6412 |
| net_win_rate | 0.4659 |
| gross_profit_factor | 1.0233 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -4.5211 |
| sortino_ratio | -1.6189 |
| max_drawdown | 0.8632 |
| cagr | -0.5391 |
| net_avg_win | 50.8821 |
| net_avg_loss | -69.2344 |
| avg_hold_time_bars | 13.8251 |
| exposure | 0.4060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
