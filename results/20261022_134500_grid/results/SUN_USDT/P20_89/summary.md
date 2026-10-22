# EMA Hourly Continuation — SUN/USDT P20_89

**Symbol:** SUN/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.3761 |
| net_win_rate | 0.3796 |
| gross_profit_factor | 0.7897 |
| gross_win_rate | 0.4336 |
| sharpe_ratio | -8.4150 |
| sortino_ratio | -3.0067 |
| max_drawdown | 0.9808 |
| cagr | -0.7902 |
| net_avg_win | 24.0264 |
| net_avg_loss | -39.0944 |
| avg_hold_time_bars | 14.0046 |
| exposure | 0.4107 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
