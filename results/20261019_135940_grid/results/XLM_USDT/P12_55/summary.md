# EMA Hourly Continuation — XLM/USDT P12_55

**Symbol:** XLM/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1058 |
| net_profit_factor | 0.4010 |
| net_win_rate | 0.4669 |
| gross_profit_factor | 0.8648 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -7.1869 |
| sortino_ratio | -3.2693 |
| max_drawdown | 0.9837 |
| cagr | -0.8043 |
| net_avg_win | 13.3250 |
| net_avg_loss | -29.1067 |
| avg_hold_time_bars | 8.0293 |
| exposure | 0.3861 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
