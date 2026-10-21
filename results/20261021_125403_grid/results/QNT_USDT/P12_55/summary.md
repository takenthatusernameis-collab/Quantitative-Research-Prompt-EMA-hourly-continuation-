# EMA Hourly Continuation — QNT/USDT P12_55

**Symbol:** QNT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 664 |
| net_profit_factor | 0.7669 |
| net_win_rate | 0.5105 |
| gross_profit_factor | 1.0449 |
| gross_win_rate | 0.5105 |
| sharpe_ratio | -2.2208 |
| sortino_ratio | -0.8221 |
| max_drawdown | 0.6393 |
| cagr | -0.3150 |
| net_avg_win | 59.5194 |
| net_avg_loss | -80.9538 |
| avg_hold_time_bars | 9.6943 |
| exposure | 0.2926 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
