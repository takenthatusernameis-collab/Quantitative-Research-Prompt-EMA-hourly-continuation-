# EMA Hourly Continuation — GTC/USDT P55_89

**Symbol:** GTC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 651 |
| net_profit_factor | 0.5618 |
| net_win_rate | 0.4762 |
| gross_profit_factor | 0.9892 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -4.8010 |
| sortino_ratio | -1.7368 |
| max_drawdown | 0.8849 |
| cagr | -0.5620 |
| net_avg_win | 36.1494 |
| net_avg_loss | -58.4998 |
| avg_hold_time_bars | 5.0952 |
| exposure | 0.1508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
