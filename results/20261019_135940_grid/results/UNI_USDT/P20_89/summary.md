# EMA Hourly Continuation — UNI/USDT P20_89

**Symbol:** UNI/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.6020 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.9279 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -4.3215 |
| sortino_ratio | -1.6223 |
| max_drawdown | 0.8655 |
| cagr | -0.5424 |
| net_avg_win | 38.0146 |
| net_avg_loss | -57.9017 |
| avg_hold_time_bars | 11.8154 |
| exposure | 0.3840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
