# EMA Hourly Continuation — XAI/USDT P26_89

**Symbol:** XAI/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.7883 |
| net_win_rate | 0.4870 |
| gross_profit_factor | 0.9779 |
| gross_win_rate | 0.4870 |
| sharpe_ratio | -1.9706 |
| sortino_ratio | -0.6288 |
| max_drawdown | 0.5949 |
| cagr | -0.2515 |
| net_avg_win | 79.2246 |
| net_avg_loss | -95.3938 |
| avg_hold_time_bars | 15.0721 |
| exposure | 0.3419 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
