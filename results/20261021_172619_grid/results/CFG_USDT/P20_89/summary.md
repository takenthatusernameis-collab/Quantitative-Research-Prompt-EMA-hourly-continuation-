# EMA Hourly Continuation — CFG/USDT P20_89

**Symbol:** CFG/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.6998 |
| net_win_rate | 0.4557 |
| gross_profit_factor | 0.8482 |
| gross_win_rate | 0.4557 |
| sharpe_ratio | -2.3160 |
| sortino_ratio | -0.6618 |
| max_drawdown | 0.5559 |
| cagr | -0.2628 |
| net_avg_win | 67.4039 |
| net_avg_loss | -80.6310 |
| avg_hold_time_bars | 26.5197 |
| exposure | 0.4894 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
