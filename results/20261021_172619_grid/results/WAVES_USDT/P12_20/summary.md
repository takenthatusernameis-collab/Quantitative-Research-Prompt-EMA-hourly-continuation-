# EMA Hourly Continuation — WAVES/USDT P12_20

**Symbol:** WAVES/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.6404 |
| net_win_rate | 0.4939 |
| gross_profit_factor | 1.0060 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -2.6618 |
| sortino_ratio | -0.6908 |
| max_drawdown | 0.5632 |
| cagr | -0.2715 |
| net_avg_win | 60.7072 |
| net_avg_loss | -92.4907 |
| avg_hold_time_bars | 5.7546 |
| exposure | 0.0853 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
