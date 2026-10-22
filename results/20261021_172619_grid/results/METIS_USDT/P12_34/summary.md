# EMA Hourly Continuation — METIS/USDT P12_34

**Symbol:** METIS/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.6558 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 0.8740 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -3.5364 |
| sortino_ratio | -1.2756 |
| max_drawdown | 0.7794 |
| cagr | -0.4425 |
| net_avg_win | 49.5393 |
| net_avg_loss | -64.8077 |
| avg_hold_time_bars | 7.1201 |
| exposure | 0.2075 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
