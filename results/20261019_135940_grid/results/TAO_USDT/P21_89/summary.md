# EMA Hourly Continuation — TAO/USDT P21_89

**Symbol:** TAO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 745 |
| net_profit_factor | 0.7290 |
| net_win_rate | 0.5020 |
| gross_profit_factor | 1.0549 |
| gross_win_rate | 0.5074 |
| sharpe_ratio | -3.2606 |
| sortino_ratio | -1.2457 |
| max_drawdown | 0.7912 |
| cagr | -0.4528 |
| net_avg_win | 56.0965 |
| net_avg_loss | -77.5742 |
| avg_hold_time_bars | 10.1275 |
| exposure | 0.3430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
