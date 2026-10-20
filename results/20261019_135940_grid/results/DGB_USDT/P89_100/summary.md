# EMA Hourly Continuation — DGB/USDT P89_100

**Symbol:** DGB/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.2475 |
| net_win_rate | 0.3484 |
| gross_profit_factor | 0.7614 |
| gross_win_rate | 0.3921 |
| sharpe_ratio | -11.3794 |
| sortino_ratio | -4.4435 |
| max_drawdown | 0.9974 |
| cagr | -0.9061 |
| net_avg_win | 13.2785 |
| net_avg_loss | -28.6872 |
| avg_hold_time_bars | 1.9111 |
| exposure | 0.0616 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
